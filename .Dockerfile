FROM python:3.11.4-bookworm

RUN pip install ipykernel
RUN pip install pandas==1.5.3
RUN pip install numpy==1.24.4
RUN pip install plotly==5.16.0
RUN pip install dash==2.12.0
RUN pip install seaborn==0.12.2
RUN pip install scikit-learn==1.3.0
RUN pip install ppscore==1.3.0
RUN pip install shap==0.42.1



CMD tail -f /dev/null