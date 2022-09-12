#include<stdio.h>

int main(){
      int N;
      int i,j,k,l;
      int target;
      int value;
      int first=0;
      int arr[1000][1000]={0};
      
      scanf("%d", &N);
      scanf("%d", &target);
      
      int last= N-1;
      int plag = N/2;
      value = N*N;
     
      while(plag>=0){
          for(i=first;i<=last;i++){
              arr[i][first] = value;
              value--;
          }
          first++;
          for(j=first;j<=last;j++){
              arr[last][j] = value;
              value--;
          }
          for(k=last-1; k>=first-1;k--){
              arr[k][last] = value;
              value--;
          }
          last--;
          for(l=last;l>=first;l--){
              arr[first-1][l] = value;
              value--;
          }
          plag--;
      }
     
      for(i=0;i<N;i++){
          for(j=0;j<N;j++){
              printf("%d ", arr[i][j]);
          }
          printf("\n");
      }
     
      for(i=0;i<N;i++){
          for(j=0;j<N;j++){
              if(arr[i][j]==target) printf("%d %d", i+1,j+1);
          }
      }
    return 0;
}

