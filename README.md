# Adaptive Multi-Format Assessment Generator with Equivalence Validation

**SDG 4: Quality Education**  
**V Semester B.E Programs - Experiential Learning Project**  
**R.V. College of Engineering | Academic Year 2025-26**

---

## 📖 Overview

An AI-powered system that automatically converts standard assessments into multiple accessible formats (simplified text, audio, braille, visual-enhanced) while maintaining semantic equivalence and difficulty alignment through automated validation.

**Problem:** Students with diverse learning needs struggle with standard text-heavy assessments. Manual creation of alternate formats takes 6-10 hours per assessment and lacks formal validation.

**Solution:** Automated multi-format generation with equivalence validation ensures accessibility without compromising assessment integrity.

---

## 🎯 Features

- ✅ **Text Simplification** - AI-powered simplification with semantic and difficulty validation
- ✅ **Text-to-Braille** - Braille-ready format conversion with structural tagging
- ✅ **Text-to-Image** - Visual diagram generation for mathematical and scientific concepts
- ✅ **Text-to-Audio** - Audio format generation (in progress)
- ✅ **Equivalence Validation** - Automated checks for semantic similarity and difficulty alignment
- ✅ **Adaptive Regeneration** - Automatic refinement until validation thresholds are met
- ✅ **Evidence Dashboard** - Comprehensive validation reports for educators

---

## 📁 Project Structure
```
5thsemel/
├── modules/
│   ├── text_simplifier/      # Text simplification with Llama 3.2 3B
│   ├── text_to_braille/       # Braille conversion engine
│   ├── text_to_image/         # Visual diagram generator
│   └── text_to_audio/         # Audio format converter (coming soon)
├── backend/                   # FastAPI integration layer (coming soon)
├── frontend/                  # React dashboard (coming soon)
└── README.md
```

---

## 🚀 Quick Start

### Text Simplifier Module
```bash
cd modules/text_simplifier
./setup.sh
python example.py
```

**Requirements:**
- Python 3.9+
- Hugging Face API token

### Text-to-Braille Module
```bash
cd modules/text_to_braille
pip install -r requirements.txt
python main.py
```

### Text-to-Image Module
```bash
cd modules/text_to_image
pip install -r requirements.txt
python main.py
```

---

## 🔬 Validation Methodology

All formats are validated using:

| Metric | Threshold | Method |
|--------|-----------|--------|
| **Semantic Similarity** | > 0.85 | Sentence-BERT (all-MiniLM-L6-v2) |
| **Difficulty Alignment** | < 10% change | Multi-factor scoring (Flesch-Kincaid + lexical analysis) |
| **Format Integrity** | 100% | Format-specific quality checks |

**Adaptive Regeneration:** If validation fails, the system automatically adjusts parameters and regenerates (max 4 attempts) before flagging for manual review.

---

## 📊 Expected Results

- **Technical Performance:**
  - Semantic similarity > 0.85 across all formats
  - Difficulty change < 10%
  - 90%+ of items pass validation within 3 attempts

- **User Impact:**
  - Reduced creation time from 6-10 hours to < 5 minutes per assessment
  - Consistent quality across all accessible formats
  - Documented equivalence for compliance

---

## 🛠️ Technology Stack

**AI/ML:**
- Meta Llama 3.2 3B (Hugging Face)
- Sentence-BERT (all-MiniLM-L6-v2)
- spaCy NLP
- matplotlib (diagram generation)

**Backend:**
- Python 3.9+
- FastAPI
- LibLouis (braille)

**Frontend:**
- React.js (planned)
- Material-UI (planned)

**All tools are free and open-source.**

---

## 👥 Team

| Name | Role | Module |
|------|------|--------|
| **Arshia Sirohi** | Team Lead | Integration & Audio |
| **Aditi Rajesh** | Developer | Text Simplification |
| **Suhani Khurana** | Developer | Text-to-Image |
| **Vinith** | Developer | Text-to-Braille |

**Institution:** R.V. College of Engineering  
**Department:** Computer Science & AI/ML  
**Course:** V Semester Experiential Learning for SDG 4

---

## 📝 Documentation

Each module contains detailed documentation:
- `modules/text_simplifier/README.md` - Text simplification setup and usage
- `modules/text_to_braille/README.md` - Braille conversion guide
- `modules/text_to_image/README.md` - Visual generation guide

---

## 🔄 Development Status

| Component | Status |
|-----------|--------|
| Text Simplifier | ✅ Complete |
| Text-to-Braille | ✅ Complete |
| Text-to-Image | ✅ Complete |
| Text-to-Audio | 🔄 In Progress |
| Backend API | 📋 Planned |
| Frontend Dashboard | 📋 Planned |
| Integration Testing | 📋 Planned |

---

## 📚 Research & References

This project addresses gaps identified in current research:
- Existing tools focus on structural accessibility without semantic validation
- No automated systems verify equivalence across multiple formats
- Manual processes lack scalability and consistency

**Key References:**
- Wilkening et al. (2024) - ACCSAMS
- Espinosa-Zaragoza et al. (2023) - Text Simplification Tools Survey
- Al-Thanyyan & Azmi (2021) - Automated Text Simplification
- Mitra (2024) - AI-Powered Adaptive Education

---

## 📄 License

MIT License

---

## 🤝 Contributing

This is an academic project for V Semester B.E Programs (ACY 2025-26). For questions or collaboration, contact the team through R.V. College of Engineering.

---

## 🎓 Acknowledgments

**Supervisor:** [Mentor Name]  
**Institution:** R.V. College of Engineering  
**Program:** Experiential Learning for SDG 4: Quality Education

---

**Go, Change the World** 🌍
