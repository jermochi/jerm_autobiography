import streamlit as st
from pathlib import Path


APP_TITLE = "Jerm's Autobiography and Portfolio"
AUTHOR_NAME = "Jervin Ryle Milleza"
FACE_IMAGE_PATH = Path("assets/face.jpg")


def show_face(image_path: Path, caption: str | None = None, use_circle_mask: bool = True) -> None:
    if image_path.exists():
        st.image(
            str(image_path),
            caption=caption,
            use_container_width=True,
            output_format="auto",
        )
    else:
        st.warning("face.jpg not found. Upload `face.jpg` to the `assets` folder to display your photo.")


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon="📚", layout="wide")

    st.title(APP_TITLE)
    st.caption("Built with Streamlit. Deployed on Streamlit Community Cloud.")

    col_photo, col_autobiography = st.columns([1, 2], gap="large")
    
    with col_photo:
        show_face(FACE_IMAGE_PATH, caption=AUTHOR_NAME)
    
    with col_autobiography:
        st.header("Autobiography")
        st.subheader(AUTHOR_NAME)
        
        with st.expander("Early Life", expanded=True):
            st.write(
                """
                My name is Jervin Ryle I. Milleza, and I was born on the day of June 9th, 2004.
                I was raised in Minglanilla, Cebu, where I lived with my older sister, my parents, and my lola.
                When I was around 3-4 years old, I was introduced to a computer and got hooked instantly.
                Playing games became one of my passions, and because of it, my eyesight got pretty bad which 
                led to lots of difficulties later on in my life.
                """
            )

        with st.expander("Education (Elementary – Senior High)", expanded=True):
            st.write(
                """
                My early years of education were almost entirely spent studying in Mary Help of Christians School in
                Minglanilla, Cebu. Those years will always be key moments to who I am as a person as I learnt so much
                from the people around me and the people who taught me there. It was only during my last year of Senior
                Highschool that I switched schools to Cebu Institute of Technology University, where I currently study at.
                """
            )

        with st.expander("College", expanded=True):
            st.write(
                """
                The course I decided on for college was Computer Science, as since I was little i've always dabbled in computers,
                so why not study what I do best. Currently I am a third year college student, and so far it has been pretty fun. 
                In my opinion, I think i could've done so much more in my first two years of college, as it's only now in my third 
                year in which i've started to join all the competitions I can join, to test myself and to go for the win.
                """
            )

        with st.expander("Biggest Achievements", expanded=True):
            st.write(
                """
                I've had few achievements in my life, so most of them I would say are part of my biggest achievements list. The ones 
                that stand out most though, is probably first the C Certification Exam where I got 2nd in my batch, and second is right now
                where I was chosen to compete for the CodeChum National Programming Competition. My life motto is "Go for the win", and it is
                very important to me as it is a reminder to myself to never half-ass anything, and always do my best.
                """
            )

        with st.expander("Current Endeavors", expanded=True):
            st.write(
                """
                As i've mentioned previously i've been joining lots of competitions right now, and I want to win them all. I've been improving during
                the National Programming Competition, and hopefully will get a perfect score in our next match. We've also applied for the Huawei Competition, and I am
                putting so much time into it studying three foreign topics. Lastly, we're currently ideating for the GCash Imagination, which I am very confident
                in, and know we will do great. Other than those, i've been chilling and having fun in life, testing out new things and enjoying the moment in every single day.
                """
            )


if __name__ == "__main__":
    main()


