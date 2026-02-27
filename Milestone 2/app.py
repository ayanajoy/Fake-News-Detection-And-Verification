from flask import Flask,render_template, request

import spacy
import sqlite3 
import re

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]","",text)
    text = re.sub(r"\s+"," ",text).strip()
    return text

def get_db():
    return sqlite3.connect("nlp.db")

@app.route("/",methods=["GET","POST"])
def home():
    tokens = lemmas = entities = []
    if request.method == "POST":
        text = request.form["text"]
        cleaned_text = clean_text(text)

        doc = nlp(cleaned_text)
        tokens = [t.text for t in doc]
        lemmas = [t.lemma_ for t in doc]

        for ent in doc.ents:
            entities.append((ent.text,ent.label_))

        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO processed_text(original_text,cleaned_text) VALUES(?,?)",
                (text,cleaned_text)
            )

            text_id = cur.lastrowid
            for e in entities:
                cur.execute(
                "INSERT INTO entities(text_id,entity,entity_type) VALUES(?,?,?)",
                (text_id,e[0],e[1])
            )
            
                conn.commit()
        except Exception as e:
            print("Database error:",e)
        
        finally:
            conn.close()
    return render_template(
        "index.html",
        tokens = tokens,
        lemmas = lemmas,
        entities=entities
    )

if __name__ == "__main__":
    app.run(debug=True)