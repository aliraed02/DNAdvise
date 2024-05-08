from configuration import llm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate






TEMPLATE = """

    Summary of idea in easy words

"DNAdvise" is a cutting-edge concept that harnesses the power of genetic information and artificial 
intelligence to provide personalized health insights and lifestyle modifications. 
Through saliva samples, individuals receive comprehensive genetic analysis, identifying potential disease risks and probabilities. 
Leveraging AI algorithms, tailored lifestyle recommendations are generated, offering actionable steps for preventive health measures. 
GeneLifestyle AI aims to empower individuals with personalized strategies for optimal well-being based on their unique genetic makeup, 
revolutionizing the approach to proactive healthcare.


These are going to be the variants that we give to AI based on the user:
· Age : {age}, Gender: {gender}, Height(cm): {heigh}, Weight(kg): {weight},
Exercise Routine: {exercise_routine}, SleepHours: {sleep_hours}, Stress Level: {stress_level},
Smoking Status: {smoking_status}, Alcohol Consumption: {alcohol_consumption}.
We will also share the genetic varient results for these conditions with AI to give results based on them:
Type 2 diabete: {type_2_diabetes}, coronary heart disease: {coronary_heart_disease}, obesity: {obesity}, 
hypertension: {hypertension}, colorectal cancer: {colorectal_cancer}, alzhimers: {alzhimers}.

### Recommendations: 
            Based on this analysis, the AI could generate personalized lifestyle modifications aimed at mitigating the risk of developing the identified health conditions. 
            These recommendations could include dietary changes, exercise routines, stress management techniques, sleep hygiene tips, and more.


### Note:
    All in all, in the end I want the ai response to be as lifestyle modification in a simplified way yet personalized.
    I want you to give out why you gave that lifestyle modification too

    ### I want the response in this format {response_json}.

"""

####################################################################################

generation_prompt = PromptTemplate(
    input_variables=["age", "gender", "heigh", "weight", "exercise_routine", "sleep_hours", "stress_level", "smoking_status", "alcohol_consumption", "type_2_diabetes", "coronary_heart_disease", "obesity", "hypertension", "colorectal_cancer", "alzhimers", "response_json"],
    template=TEMPLATE,
)


#################################################################################################


generation_chain = LLMChain(llm=llm, prompt=generation_prompt, output_key="response", verbose=True)
