class MinStack {
    private Stack<Integer> stack;
    private int minimum;
    public MinStack() {
          stack = new Stack<>();
          minimum=Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        if(val<=minimum){
            stack.push(minimum);
            minimum=val;
        }
        stack.push(val);
        
        
    }
    
    public void pop() {
        if(stack.isEmpty()){
            return;
        }
        if(stack.pop()==minimum){
            minimum=stack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
        
    }
    
    public int getMin() {
       return minimum;
    }
}
