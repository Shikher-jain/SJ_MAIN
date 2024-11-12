def detect_sequence(transitions):
  state={}
  initial=None
  final=None
  Outputs=[]
  seq=[]
  
  for trans in transitions:
    #STATES
    present,next,input,output =trans.split()
    input=int(input)
    output=int(output)
    
    if initial is None:
      initial = present
     
    
    
for i, transitions in enumerate(tc,1):
  detectSEQ , dectectTYPE= detect_sequence(transitions)
  print(f"TestCase {i}")
  print(detectSEQ)
  print(dectectTYPE)
  print()