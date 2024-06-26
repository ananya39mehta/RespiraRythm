import streamlit as st

def home():
    st.title('Home')
    st.header('Welcome to Respira Rhythm Classifier!')
    st.write("""
        Thank you for using this application. By visiting this page, you've joined us in the important cause of proactively monitoring your health.
        \n\n
        Lung diseases are a major global issue, contributing to millions of deaths yearly. Respiratory problems can worsen over time.
        \n\n
        Prevention is crucial. We've developed Respira Rhythm—an ML-based model to assess your breathing health.
        It's accurate, reliable, and trustworthy, trained on authentic data for optimum accuracy.
    """)

def predict():
    st.title('Predict')
    st.write('Welcome to the Predict page!')

def about_us():
    st.title('About Us')
    st.write('Welcome to the About Us page!')
    st.subheader('Meet Our Team:')
    
    # Display images and details of founders
    founders = [
        {
            'name': 'Ananya Mehta',
            'image_url': 'https://tse3.explicit.bing.net/th?id=OIP.VIplnCsGqHdRbTyZj1sJOQHaHa&pid=Api&P=0&h=180',
            'description': 'AI enthusiast with a passion for healthcare innovation.'
        },
        {
            'name': 'Aparna Iyer',
            'image_url': 'https://tse3.explicit.bing.net/th?id=OIP.VIplnCsGqHdRbTyZj1sJOQHaHa&pid=Api&P=0&h=180',
            'description': 'ML engineer focused on leveraging technology for social impact.'
        },
        {
            'name': 'Deeksha Mandal',
            'image_url': 'https://tse3.explicit.bing.net/th?id=OIP.VIplnCsGqHdRbTyZj1sJOQHaHa&pid=Api&P=0&h=180',
            'description': 'Data science advocate dedicated to improving public health.'
        },
        {
            'name': 'Dhwani Bhavankar',
            'image_url': 'https://tse3.explicit.bing.net/th?id=OIP.VIplnCsGqHdRbTyZj1sJOQHaHa&pid=Api&P=0&h=180',
            'description': 'Tech enthusiast with a vision for accessible healthcare solutions.'
        }
    ]
    # Create a grid layout using columns
    num_columns = 2  # Number of columns in the grid
    image_width = 150  # Width of each image in pixels
    
    with st.container():
        for i in range(0, len(founders), num_columns):
            cols = st.columns(num_columns)
            for j in range(num_columns):
                if i + j < len(founders):
                    founder = founders[i + j]
                    cols[j].write(f"**{founder['name']}**")
                    cols[j].image(founder['image_url'], width=image_width)
                    cols[j].write(founder['description'])

def main():
    option = st.sidebar.button('Home')
    if option:
        home()
    
    option = st.sidebar.button('Predict')
    if option:
        predict()
    
    option = st.sidebar.button('About Us')
    if option:
        about_us()

if __name__ == "__main__":
    main()
