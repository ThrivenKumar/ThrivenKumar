
public class variableWindow{
    public static void largestSubArray(int n, int[] numbers,int key){
        int temp,sum=0;
        loop1: for (int i=n-1;i>0;i--){
            sum=0;
            for(int j=0;j<=n-i;j++){
                if(j==0){
                    for(int k=0;k<i;k++){
                        sum+=numbers[k];
                    }
                }
                else{
                    sum+=numbers[j+i-1];
                    sum-=numbers[j-1];
                }
                if(sum==key){
                    System.out.println("Largest sub array: "+ i + " "+ j);
                    break loop1;
                }
            }
        }
    }
    public static void main(String[] args){
        int numbers[]=new int[]{1,2,3,4,5};
        largestSubArray(5,numbers,15);
    }
}