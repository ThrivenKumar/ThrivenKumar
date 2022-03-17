import java.util.*;
public class ReversenotPrime{

    public int prime(int n){
        int i,m=0,flag=0;   
        m=n/2;      
        if(n==0||n==1){  
            return 0;   
        }else{  
            for(i=2;i<=m;i++){      
                if(n%i==0){      
                    return 0;     
                }      
            }      
            if(flag==0)  {
                return 1;
            }  
        }
        return 0;
    }
    public static void main(String args[]){
        ReversenotPrime r=new ReversenotPrime();
        Scanner s=new Scanner(System.in);
        int num=s.nextInt();
        int[] arr=new int[num];
        int[] result=new int[num];
        int count=0;
        for(int i=0;i<num;i++){
            arr[i]=s.nextInt();
        }
        for(int j=0;j<num;j++){
            int flag1=r.prime(arr[j]);
            int reverse = 0;  
            while(arr[j] != 0)   
            {  
                int remainder = arr[j] % 10;  
                reverse = reverse * 10 + remainder;  
                arr[j] = arr[j]/10;
            }
            if( flag1==0){
                int flag2=r.prime(reverse);
                if (flag2==1){
                    result[count++]=arr[j];
                }
            }
        }
        for(int i=0;i<num;i++){
            System.out.println(result[i]);
        }
    }
}