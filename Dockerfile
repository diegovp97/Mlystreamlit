FROM python:3.8

RUN pip install pandas scikit-learn streamlit

COPY src/app.py /app/
COPY src/modelo_diabetes.sav /app/

WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.py"]

