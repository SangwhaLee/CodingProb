function solution(s)
{
    let answer = -1;
    
    let stack = [];
    let top = -1;
    
    for(let i of s){
        if(stack.length === 0){
            stack.push(i);
            top++;
        }
        else{
            if(stack[top] === i){
                stack.pop()
                top--;
            }
            else{
                stack.push(i)
                top++;
            }   
        }
    }
    
    if(stack.length === 0){
        answer = 1
    }
    else{
        answer = 0 
    }

    return answer;
}