def serve_chai():
  yield "chai"
  yield "chai 1"
  yield "chai 2"
  yield "chai 3"
  
stall = serve_chai()
print(stall)

for chai in stall:
    print(chai)
