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