# PROFILE BANNER

> **Profile.py**
```python
from collections import defaultdict

import charan
languages = ['Python (3 years)', 'SQL (2 years)', 'Bash (3 years)']
tech = ['AWS', 'LangChain', 'ChromaDB', 'RAG', 'Docker', 'MLFlow', 'SKlearn', 'Pandas', 'NumPy',
        'Matplotlib', 'TensorFlow', 'PyTorch', 'FastAPI', 'Flask', 'Streamlit', 'Git', 'DVC']
data_analysis = ['Data Cleaning','Feature Engineering','EDA','Statistical Analysis']
connect = { 'LinkedIn': 'https://www.linkedin.com/in/CodeWithCharan/',
            'GitHub': 'https://github.com/CodeWithCharan',
            'Portfolio': 'https://codewithcharan.github.io/My-Portfolio/'}
connect_with_me = defaultdict(list, connect)
if __name__ == "__main__":
    charan.combine([languages, tech, data_analysis, connect_with_me])
```

> **charan.py**
```python
def combine(data):
    
    languages, tech, data_analysis, connect_with_me = data
    
    # Print languages
    print("Languages:")
    for language in languages:
        print("-", language)

    # Print technologies
    print("\nTechnologies:")
    for t in tech:
        print("-", t)
    
    # Print data analysis
    print("\nData Analysis:")
    for da in data_analysis:
        print("-", da)
    
    # Print connection information
    print("\nConnect with me:")
    for platform, link in connect_with_me.items():
        print(f"- {platform}: {link}")
```

> **Terminal**
```bash
>>> python Profile.py
Languages:
- Python (3 years)
- SQL (2 years)
- Bash (3 years)

Technologies:
- AWS
- LangChain
- ChromaDB
- RAG
- Docker
- MLFlow
- SKlearn
- Pandas
- NumPy
- Matplotlib
- TensorFlow
- PyTorch
- FastAPI
- Flask
- Streamlit
- Git
- DVC

Data Analysis:
- Data Cleaning
- Feature Engineering
- EDA
- Statistical Analysis

Connect with me:
- LinkedIn: https://www.linkedin.com/in/CodeWithCharan/
- GitHub: https://github.com/CodeWithCharan
- Portfolio: https://codewithcharan.github.io/My-Portfolio/
```