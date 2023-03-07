function solution(n) {
    let Fibo = [0,1];
    
    for(let i=2; i<=n ;i++){
        let sum = Fibo[i-1] + Fibo[i-2];
        Fibo.push(sum % 1234567);
    }
    
    let answer = Fibo[n]%1234567;
    return answer;
}