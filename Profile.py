from collections import defaultdict

import charan
tools = ['Python3','TensorFlow','FastAPI','Flask','Streamlit','Scikit-learn','Pandas','NumPy',
        'MLflow','CI/CD','DagsHub','Git','DVC','MySQL','Matplotlib','Seaborn','HTML','CSS']
expertise = ['Datacleaning','Featureengineering','EDA','Datapreprocessing','Modeling','ModelDeployment']
connect = { 'LinkedIn': 'https://www.linkedin.com/in/codewithcharan/',
            'Email': 'thoutamsricharan@gmail.com',
            'GitHub': 'https://github.com/CodeWithCharan',
            'Portfolio': 'https://codewithcharan.github.io/My-Portfolio/'}
connect_with_me = defaultdict(list)
connect_with_me.update(connect)
if __name__ == "__main__":
    charan.combine([tools, expertise, connect_with_me])
