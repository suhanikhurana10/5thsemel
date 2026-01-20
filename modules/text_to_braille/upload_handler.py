from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid

# Pipeline imports
from app.extractor import extract_text          # Step 3
from app.preprocessor import clean_text         # Step 4
from app.classifier import classify_text        # Step 5
from app.tagger import apply_tags               # Step 6
from app.braille_engine import convert_to_braille  # Step 7

router = APIRouter(prefix="/upload", tags=["Upload"])

# Directories
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Allowed formats
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}


@router.post("/")
async def upload_assessment(file: UploadFile = File(...)):
    # 1️⃣ Validate file extension
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX, and TXT files are supported"
        )

    # 2️⃣ Save uploaded file
    unique_name = f"{uuid.uuid4()}{ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # 3️⃣ Extract text
    raw_text = extract_text(file_path)
    if not raw_text or raw_text.strip() == "":
        raw_text = "No extractable text found (possible scanned PDF)."

    # 4️⃣ Clean text
    cleaned_text = clean_text(raw_text)

    # 5️⃣ Classify structure
    classified_output = classify_text(cleaned_text)

    # 6️⃣ Apply Braille-ready tags
    tagged_output = apply_tags(classified_output)

    # 7️⃣ Convert to Braille (.brf)
    braille_file_path = convert_to_braille(tagged_output, OUTPUT_DIR)

    # 8️⃣ Final response
    return {
        "message": "✅ File uploaded and converted to Braille successfully!",
        "original_filename": file.filename,
        "stored_filename": unique_name,
        "uploaded_file_path": file_path,

        # Previews for verification
        "raw_text_preview": raw_text[:300],
        "cleaned_text_preview": cleaned_text[:300],
        "classification_preview": classified_output[:10],
        "tagged_preview": tagged_output[:10],

        # ✅ FINAL OUTPUT
        "braille_file_path": braille_file_path
    }
