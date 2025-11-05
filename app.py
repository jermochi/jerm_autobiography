import streamlit as st
import base64
from pathlib import Path


APP_TITLE = "Jerm's Autobiography and Portfolio"
AUTHOR_NAME = "Jervin Ryle Milleza"
FACE_IMAGE_PATH = Path("assets/face.jpg")
GITHUB_LOGO_PATH = Path("assets/github_logo.png")
FACEBOOK_LOGO_PATH = Path("assets/facebook_logo.png")
INSTAGRAM_LOGO_PATH = Path("assets/instagram_logo.png")


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

    st.divider()

    # Portfolio section
    st.header("Portfolio")
    
    # Summary
    st.subheader("Summary")
    st.write(
        """
        Jervin Ryle I. Milleza is a 3rd year college student currently enrolled in the course Bachelor of Science in Computer Science at
        Cebu Institute of Technology - University. He specializes in front-end development, bringing forth designs that are sleek yet provides
        the users with easy times. He is also proficient in competitive programming, solving problems as a hobby and solving them with haste. 
        He believes that anything can be won, with the right amount of effort and confidence.   
        """
    )
    
    st.markdown("\n")
    
    # Social links with logos
    st.subheader("Connect with Me")
    col_gh, col_fb, col_ig = st.columns(3)
    
    with col_gh:
        if GITHUB_LOGO_PATH.exists():
            # Read image as base64 for embedding in HTML
            with open(GITHUB_LOGO_PATH, "rb") as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
            st.markdown(
                f'''
                <div style="text-align: center;">
                    <a href="https://github.com/jermochi" target="_blank" style="text-decoration: none;">
                        <div style="width: 80px; height: 80px; background-color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                            <img src="data:image/png;base64,{img_data}" width="50" height="50" style="display: block;">
                        </div>
                        <p style="margin-top: 10px; color: #ffffff;">GitHub</p>
                    </a>
                </div>
                ''',
                unsafe_allow_html=True
            )
        else:
            st.markdown("[GitHub](https://github.com/jermochi)")
    
    with col_fb:
        if FACEBOOK_LOGO_PATH.exists():
            with open(FACEBOOK_LOGO_PATH, "rb") as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
            st.markdown(
                f'''
                <div style="text-align: center;">
                    <a href="https://facebook.com/jrvnryle" target="_blank" style="text-decoration: none;">
                        <div style="width: 80px; height: 80px; background-color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                            <img src="data:image/png;base64,{img_data}" width="50" height="50" style="display: block;">
                        </div>
                        <p style="margin-top: 10px; color: #ffffff;">Facebook</p>
                    </a>
                </div>
                ''',
                unsafe_allow_html=True
            )
        else:
            st.markdown("[Facebook](https://facebook.com/your-profile)")
    
    with col_ig:
        if INSTAGRAM_LOGO_PATH.exists():
            with open(INSTAGRAM_LOGO_PATH, "rb") as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
            st.markdown(
                f'''
                <div style="text-align: center;">
                    <a href="https://instagram.com/jrvnryle" target="_blank" style="text-decoration: none;">
                        <div style="width: 80px; height: 80px; background-color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                            <img src="data:image/png;base64,{img_data}" width="50" height="50" style="display: block;">
                        </div>
                        <p style="margin-top: 10px; color: #ffffff;">Instagram</p>
                    </a>
                </div>
                ''',
                unsafe_allow_html=True
            )
        else:
            st.markdown("[Instagram](https://instagram.com/your-handle)")
    
    st.markdown("\n")
    
    # Education and Experience side by side
    col_edu, col_exp = st.columns(2, gap="large")
    
    with col_edu:
        st.subheader("Education")
        st.markdown(
            """
            - **Elementary School**  
              Mary Help of Christians School — Minglanilla, Cebu  
              *2009 - 2016*
            
            - **Junior High School**  
              Mary Help of Christians School — Minglanilla, Cebu  
              *2016 - 2021*
            
            - **Senior High School**  
              Cebu Institute of Technology University — Cebu City  
              *2021 - 2022*
            
            - **College**  
              Cebu Institute of Technology University — Cebu City  
              Bachelor of Science in Computer Science (BSCS)  
              2022 - Present
            """
        )
    
    with col_exp:
        st.subheader("Experience")
        
        col_competitions, col_apps = st.columns(2, gap="medium")
        
        with col_competitions:
            st.markdown("**Competitions & Roles**")
            st.markdown(
                """
                - **Main Role**  
                  Front-end Developer / UI & UX
                  
                - **Competition Participant**  
                  CodeChum National Programming Competition  
                
                - **Competition Participant**  
                  Huawei Competition  
                
                - **C Certification Exam**  
                  2nd Place in Batch Year 2023
                
                - **Community Developer Officer | GDG**  
                  Specializes in community development
                """
            )
        
        with col_apps:
            st.markdown("**Apps & Projects**")
            st.markdown(
                """
                - **Project Team Member**  
                  GCash Imagination  
                
                - **Hygienix App**  
                  Game App used for Nursing student's research
                
                - **AniMo App**  
                  App used for helping farmers combat food security problems
                
                - **LockedIn App**  
                  News App to get the latest information in the eSports scene
                """
            )


if __name__ == "__main__":
    main()


