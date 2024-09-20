import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def main():
    st.set_page_config(page_title="AI-Powered Textbot Case Study", layout="wide", page_icon="case_study/mb_logo_white copy.png")
    
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
    st.sidebar.image("case_study/mb_logo_white copy.png")
    st.sidebar.divider()
    st.sidebar.header("Menu")
    selection = st.sidebar.radio("", sections)
    
    # Content for each section
    if selection == "Overview":
        st.header("Overview")
        st.write("""
        moonbird developed a cutting-edge AI-powered textbot designed to streamline customer interactions for a healthcare client. 
        The textbot not only automates responses to common inquiries but also integrates seamlessly with human representatives 
        for more complex queries. This intelligent solution improves customer satisfaction, enhances operational efficiency, and 
        empowers human resources to focus on high-value tasks.
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
        Our client is a leader in the healthcare space, focused on providing high-quality patient care through innovative 
        technology and proprietary treatment methods. Their core objectives included driving leads, improving patient outcomes, 
        and optimizing internal workflows by minimizing the time spent on routine customer inquiries.
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
        The client faced multiple challenges in their operational processes:
        1. Resource constraints: Human representatives were overwhelmed with repetitive queries, leaving little time for strategic tasks like lead generation.
        2. Data silos: The client used multiple platforms, making it difficult to provide a unified customer experience.
        3. Scalability issues: Handling an increasing number of inquiries required a solution that could scale without needing additional personnel.
        4. Consistency and safety: AI-generated responses had to align with service standards and avoid errors while addressing sensitive healthcare-related queries​.
       """)
        # In addition, the technical challenges in implementing the AI-powered textbot were as follows:
        # 1. Integrating LLM capabilities into the existing process managed by human representatives
        # 2. Connecting multiple systems and drawing from multiple data sources
        # 3. Implementing human-in-the-loop for specific use cases (e.g., scheduling, location questions)
        # 4. Equipping the LLM with context from the wider conversation
        # 5. Ensuring ongoing monitoring of LLM responses
        # """)
        
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
                The AI-powered textbot was engineered with a focus on accuracy, scalability, and seamless system integration. The technical architecture included the following key elements:
                """)
            st.subheader("Input Processing and Classification:")
            st.write("""The bot’s NLP capabilities analyzed incoming messages to understand the context and classify the type of inquiry (e.g., scheduling, treatment information, general questions).
                     """)
            st.subheader("Sequential Prompt Chaining:")
            st.write("""Complex customer inquiries were handled using prompt chaining, where each query was broken down into smaller tasks. This method ensured accuracy by allowing the system to process each component step-by-step before generating a response.
                     """)
            st.subheader("Human-in-the-Loop Integration:")
            st.write("""CFor cases requiring human intervention (e.g., scheduling appointments or answering location-based queries), the bot automatically routed the conversation to a human representative through Slack, ensuring seamless transitions​.
                     """)
            st.subheader("Multi-Source Data Integration:")
            st.write("""The system connected to multiple data sources, including:""")
            st.write("*Text platforms for sending and receiving messages")
            st.write("*BigQuery for logging and monitoring dashboards")
            st.write("*Slack for human assistance integration")
            st.write("""This multi-system connectivity ensured that all responses were informed by accurate and up-to-date information across platforms.
                     """)
            st.subheader("Response Generation and Safety Checks:")
            st.write("""The LLM (Large Language Model) was used to generate responses while incorporating safety checks to prevent hallucinations and ensure that all replies adhered to client-specific guidelines. This process reduced errors and made the responses both reliable and safe​.
                     """)
            st.subheader("Scalability Architecture:")
            st.write("""The system was built to be scalable, enabling it to handle increasing volumes of customer inquiries without performance degradation. This architecture is easily adaptable for multiple clinics, enhancing the client's ability to grow without the need for additional resources
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
            st.image("case_study/flowChart_caseStudy.png")
        
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
                "description": "Human representatives were freed from handling repetitive tasks, allowing them to focus on more strategic activities like lead generation and patient care",
                "icon": "🎯"
            },
            {
                "title": "Faster Response Times",
                "description": "Automation significantly reduced the time it took to respond to customer inquiries, resulting in higher customer satisfaction.",
                "icon": "😊"
            },
            {
                "title": "Increased Operational Efficiency",
                "description": "Automation of routine queries streamlined the client’s operations and reduced the overall workload on staff​.",
                "icon": "⚙️"
            },
            {
                "title": "Positive Team Feedback",
                "description": "The integration of AI resulted in higher job satisfaction, with team members able to focus on more fulfilling, value-added tasks.",
                "icon": "👍"
            },
            {
                "title": "Scalable Solution",
                "description": "The textbot seamlessly handled increased interaction volumes without compromising the quality of responses, positioning the client for sustainable growth.",
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
                "description": "Automating repetitive tasks enables human resources to focus on more critical areas.",
                "icon": "⚡"
            },
            {
                "title": "Balance Automation with a Human Touch",
                "description": "While AI excels in many complex tasks, maintaining human oversight for complex scenarios ensures high quality of.",
                "icon": "⚖️"
            },
            {
                "title": "Prioritize Accuracy and Safety",
                "description": "Continuous monitoring and safety checks are critical for ensuring reliable AI performance, especially in regulated industries like healthcare​.",
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
