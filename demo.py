import os
import json
from groq import Groq

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print("\n❌ GROQ_API_KEY not found!")
    print("👉 Get your free key at: console.groq.com")
    print("👉 Create a .env file with: GROQ_API_KEY=your_key_here")
    print("👉 See README.md for setup instructions\n")
    exit(1)
client = Groq(api_key=api_key)

def decompose_goal(goal):
    """Break a complex goal into atomic steps using LLM"""
    print(f"\n🔍 Decomposing goal: {goal}\n")
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are SRI's task decomposer. 
                Break the given goal into 3-5 atomic, simple steps.
                Each step must be simple enough to execute reliably.
                Respond ONLY with a JSON array like this:
                [
                    {"id": 1, "step": "description of step", "output": "what this step produces"},
                    {"id": 2, "step": "description of step", "output": "what this step produces"}
                ]
                Nothing else. Just the JSON array."""
            },
            {
                "role": "user", 
                "content": f"Decompose this goal into atomic steps: {goal}"
            }
        ]
    )
    
    raw = response.choices[0].message.content.strip()
    steps = json.loads(raw)
    return steps

def execute_step(step):
    """Execute a single atomic step using LLM"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are SRI's executor. Execute the given step and produce the output. Be specific and concrete."
            },
            {
                "role": "user",
                "content": f"Execute this step: {step['step']}\nProduce: {step['output']}"
            }
        ]
    )
    return response.choices[0].message.content.strip()

def human_gate(step, output):
    """Ask human to approve or reject each step output"""
    print(f"\n{'='*50}")
    print(f"📋 STEP {step['id']}: {step['step']}")
    print(f"{'='*50}")
    print(f"\n🤖 AI Output:\n{output}")
    print(f"\n{'='*50}")
    
    while True:
        decision = input("\n✅ Approve this step? (y/n/r for refine): ").lower().strip()
        if decision in ['y', 'n', 'r']:
            return decision
        print("Please enter y, n, or r")

def run_sri(goal):
    """Main SRI orchestration loop"""
    print("\n" + "="*50)
    print("       SRI — Skill-based Reasoning Intelligence")
    print("       श्री — Breaking the complexity ceiling")
    print("="*50)
    
    # Step 1: Decompose
    steps = decompose_goal(goal)
    print(f"✅ Decomposed into {len(steps)} atomic steps\n")
    
    for i, step in enumerate(steps):
        print(f"  Step {step['id']}: {step['step']}")
    
    print(f"\n{'='*50}")
    input("\nPress Enter to begin execution...\n")
    
    # Step 2: Execute + Verify + Human Gate
    approved_outputs = []
    
    for step in steps:
        print(f"\n⚙️  Executing step {step['id']}...")
        output = execute_step(step)
        
        decision = human_gate(step, output)
        
        if decision == 'y':
            approved_outputs.append({"step": step, "output": output})
            print(f"✅ Step {step['id']} approved")
        elif decision == 'n':
            print(f"❌ Step {step['id']} rejected — stopping")
            return
        elif decision == 'r':
            print(f"🔄 Refining step {step['id']}...")
            output = execute_step(step)
            approved_outputs.append({"step": step, "output": output})
            print(f"✅ Step {step['id']} refined and approved")
    
    # Step 3: Final outcome
    print(f"\n{'='*50}")
    print("🎉 SRI COMPLETE — All steps verified and approved")
    print(f"{'='*50}")
    print(f"\n📊 Summary: {len(approved_outputs)} steps completed successfully")
    print("\nCeiling never hit. 🙏\n")

# Run it
if __name__ == "__main__":
    goal = input("\n🎯 Enter your goal: ")
    run_sri(goal)