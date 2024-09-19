import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def main():
    st.set_page_config(page_title="AI-Powered Textbot Case Study", layout="wide", page_icon="mb_logo_white copy.png")
    
    st.title("AI-Powered Textbot Case Study")
    st.divider()
    
    # Sidebar for navigation
    sections = [
        "Overview",
        "Client Background",
        "Challenge",
        "Solution",
        "Results",
        "Key Takeaways"
    ]
    st.sidebar.image("mb_logo_white copy.png")
    st.sidebar.divider()
    st.sidebar.header("Menu")
    selection = st.sidebar.radio("", sections)
    
    # Content for each section
    if selection == "Overview":
        st.header("Overview")
        st.write("""
        We developed an AI-powered capability to manage text message interactions with leads who signed up on the client's website. 
        The textbot was designed with the following key capabilities:
        """)
        
        # Native Streamlit visualization for textbot capabilities
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="Product Knowledge", value="100%", delta="Comprehensive")
            st.markdown("**Multi-source Integration**")
            st.caption("Pulls information from various data sources")
            st.markdown("**Multiple Output Destinations**")
            st.caption("Connects to Slack for pulling humans-in-the-loop; connects to BigQuery for monitoring dashboards; connects to the text platform for receiving and sending text messages.")
            
        with col2:
            st.metric(label="Accuracy", value="99%", delta="High Precision")
            st.markdown("**Real-time Responses**")
            st.caption("Delivers relevant answers instantly with accurate information and contextual awareness")
        
        st.info("""
        The AI-powered textbot significantly enhances customer interactions by providing quick, 
        accurate, and contextually relevant responses, improving overall user experience and operational efficiency.
        """)
        
    elif selection == "Client Background":
        st.header("Client Background")
        st.write("""
        Our client operates in the healthcare space with the following key goals:
        """)
        
        # Client goals with importance ratings
        goals = {
            'Drive leads to schedule appointments': 10,
            'Facilitate treatment for various maladies': 8,
            'Utilize proprietary product and method': 9,
            'Improve patient outcomes': 9
        }
        
        # Visualize goals using Streamlit components
        for goal, importance in goals.items():
            st.subheader(goal)
            col1, col2, col3 = st.columns([2, 6, 2])
            with col1:
                st.write("Priority:")
            with col2:
                st.progress(importance / 10)
            with col3:
                st.write(f"{importance}")
            
            # Add some space between goals
            st.write("")
        
        # Additional context
        st.info("""
        Our client is committed to revolutionizing healthcare delivery through innovative 
        technology and personalized patient care. By leveraging AI-powered solutions, 
        they aim to streamline the patient journey from initial contact to successful treatment.
        """)

        # # Key metrics or facts about the client
        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     st.metric(label="Years in Operation", value="15+")
        # with col2:
        #     st.metric(label="Clinic Partners", value="500+")
        # with col3:
        #     st.metric(label="Patients Served", value="100k+", delta="Annual")
        
    elif selection == "Challenge":
        st.header("Challenge")
        st.write("""
        The main challenges in implementing the AI-powered textbot were:
        1. Integrating LLM capabilities into the existing process managed by human representatives
        2. Connecting multiple systems and drawing from multiple data sources
        3. Implementing human-in-the-loop for specific use cases (e.g., scheduling, location questions)
        4. Equipping the LLM with context from the wider conversation
        5. Ensuring ongoing monitoring of LLM responses
        """)
        
        # Visualization: Challenge Complexity
        challenges = ['System Integration', 'Human-in-the-loop', 'Contextual Understanding', 'Response Monitoring', 'Multi-system Connectivity']
        complexity = [8, 7, 9, 8, 9]
        fig = go.Figure(data=go.Scatterpolar(
          r=complexity,
          theta=challenges,
          fill='toself'
        ))
        fig.update_layout(
          polar=dict(
            radialaxis=dict(
              visible=True,
              range=[0, 10]
            )),
          showlegend=False,
          title='Challenge Complexity (1-10 scale)'
        )
        st.plotly_chart(fig)
        
    elif selection == "Solution":
        st.header("Solution")
        sol, solImage = st.columns(2)
        with sol:
            st.write("""
            Our team architected a solution with the following key features:
            - Fast, accurate, predictable, and safe responses
            - Significant mitigation of LLM hallucinations
            - Seamless integrations with all systems, scalable across multiple clinics
            - Bite-sized classification tasks using sequential chains of prompts and code processing
            - Prioritization of accuracy, safety, and predictability
            - Leveraging LLMs for natural language processing
            """)
            
            st.subheader("Solution Architecture Flow")
            
            # Define the stages of the solution with their details
            stages = {
                "Input Processing": "Analyzes and preprocesses user input for efficient handling.",
                "Classification": "Categorizes the input to determine appropriate response strategy.",
                "Prompt Chaining": "Constructs a series of prompts to guide the LLM's response.",
                "Response Generation": "Utilizes LLM to create a contextually relevant response.",
                "Safety Check": "Ensures the generated response adheres to safety and accuracy standards.",
                "Output Delivery": "Formats and sends the final response to the user."
            }
            
            # Display each stage as an expander
            for stage, details in stages.items():
                with st.expander(stage):
                    st.write(details)
            
            st.write("")
            st.info("""
            This architecture ensures a systematic approach to processing user inputs and generating 
            safe, accurate responses. Each stage is designed to enhance the overall quality and 
            reliability of the AI-powered textbot interactions.
            """)

        with solImage:
            st.image("flowChart_caseStudy.png")
        
    elif selection == "Results":
        st.header("Results")
        st.write("""
        The implementation of the AI-powered textbot capability has yielded significant benefits 
        across various aspects of our client's operations:
        """)

        # Define the key results
        results = [
            {
                "title": "Improved Resource Allocation",
                "description": "Human representatives shifted focus to higher-value tasks such as lead generation and deal closings.",
                "icon": "🎯"
            },
            {
                "title": "Enhanced Customer Experience",
                "description": "Faster response times and more accurate information improved overall customer satisfaction.",
                "icon": "😊"
            },
            {
                "title": "Increased Operational Efficiency",
                "description": "Automation of routine inquiries led to smoother operations and reduced workload on staff.",
                "icon": "⚙️"
            },
            {
                "title": "Positive Team Feedback",
                "description": "Staff reported high satisfaction with the AI assistance, noting reduced stress and more fulfilling work.",
                "icon": "👍"
            },
            {
                "title": "Scalable Solution",
                "description": "The textbot seamlessly handled increased inquiry volumes without compromising quality.",
                "icon": "📈"
            }
        ]

        # Display results in an attractive format
        for result in results:
            st.subheader(f"{result['icon']} {result['title']}")
            st.markdown(f"<div style='margin-left: 40px;'>{result['description']}</div>", unsafe_allow_html=True)
            st.write("")  # Add some space between results

        # Add a summary statement
        st.success("""
        Overall, the AI-powered textbot has significantly enhanced our client's ability to manage customer 
        interactions efficiently, allowing for better resource utilization and improved customer satisfaction. 
        The solution has proven to be robust, scalable, and has received overwhelmingly positive feedback 
        from both staff and customers.
        """)

        # Add a note about ongoing monitoring
        st.info("""
        **Note:** We continue to monitor the performance of the AI components, ensuring ongoing accuracy, 
        predictability, and safety in all interactions. This commitment to quality assurance guarantees 
        that the benefits realized will be sustained and improved over time.
        """)
        
    elif selection == "Key Takeaways":
        st.header("Key Takeaways")
        st.write("""
        Our experience with this AI-powered textbot project has provided valuable insights 
        for future AI integration in customer service. Here are the key takeaways:
        """)

        takeaways = [
            {
                "title": "AI Enhances Operational Efficiency",
                "description": "Integration of AI in customer interactions significantly improves response times and handling capacity.",
                "icon": "⚡"
            },
            {
                "title": "Balance Automation with a Human Touch",
                "description": "While AI excels in many complex tasks, maintaining human oversight for complex scenarios ensures high quality of.",
                "icon": "⚖️"
            },
            {
                "title": "Prioritize Accuracy and Safety",
                "description": "Careful system design focusing on precision and safety mitigates risks associated with AI hallucinations.",
                "icon": "🛡️"
            },
            {
                "title": "Leverage LLMs for Specific Tasks",
                "description": "Using LLMs for targeted, well-defined tasks yields better results than broad, open-ended implementations.",
                "icon": "🎯"
            },
            {
                "title": "Continuous Monitoring is Crucial",
                "description": "Ongoing performance monitoring and improvement are essential for maintaining AI system effectiveness.",
                "icon": "📊"
            },
            {
                "title": "Seamless Integration is Key",
                "description": "Effective AI solutions require smooth integration with existing systems and workflows.",
                "icon": "🔗"
            },
            {
                "title": "Empower Human Resources",
                "description": "AI implementation allows shifting human resources to high-value tasks, improving overall business outcomes.",
                "icon": "💪"
            }
        ]

        # Create two columns
        col1, col2 = st.columns(2)

        # Display takeaways in two columns
        for i, takeaway in enumerate(takeaways):
            with col1 if i % 2 == 0 else col2:
                with st.expander(f"{takeaway['icon']} {takeaway['title']}"):
                    st.write(takeaway['description'])
                    st.write("")  # Add some space

        # Add a concluding statement
        st.success("""
        These key takeaways underscore the transformative potential of AI in customer service 
        when implemented thoughtfully. By focusing on these areas, organizations can harness 
        the power of AI to enhance customer experiences, improve operational efficiency, and 
        drive business growth.
        """)

        # Add a forward-looking statement
        st.info("""
        **Looking Ahead:** As AI technology continues to evolve, we anticipate even more 
        innovative applications in customer service. Our team remains committed to staying 
        at the forefront of these developments, ensuring our clients benefit from cutting-edge, 
        responsible AI solutions.
        """)

if __name__ == "__main__":
    main()