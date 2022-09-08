#include<stdio.h>

int main() {
    long term=1;
    int T;
    int i;
    long start,end;
    long df=0;
    long cnt=1;
    
    scanf("%d", &T);
    
    for(i=0;i<T;i++){
        term=1;
        df=0;
        cnt=1;
        
        scanf("%ld %ld", &start, &end);
        
        while(end-start>term){
            df++;
            
            term += df;
            cnt++;
            if(term>=end-start) break;
            
            term += df;
            cnt++;
        }
        if(term>end-start) cnt--;
        printf("%d\n", cnt);
    }
    return 0;
}