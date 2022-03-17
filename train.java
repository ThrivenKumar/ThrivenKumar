import java.util.*;
class train{
  public static void main(String args[]){
    int[] a=new int[100];
    int[] b=new int[100];
    int[] c=new int[100];
    int[] d=new int[100];
    int count3=0;
    int trains=0,i,j,count=0,count2=0;
    String data1,data2;
    Scanner s=new Scanner(System.in);
    try{
      trains=Integer.parseInt(args[0]);
    }
    catch(Exception e){
      System.exit(0);
    }
    for(i=1;i<=trains;i++){
      data1=args[++count3];
      data2=args[++count3];
      a[i]=Integer.parseInt(data1);
      b[i]=Integer.parseInt(data2);
      for(j=0;j<10;j++){
        if(c[j]<a[i]&&(c[j]+d[j])<a[i]){
          c[j]=a[i];
          d[j]=b[i];
          break;
        }
        else if(c[j]>a[i]&&(a[j]+b[j])<c[i]){
          c[j]=a[i];
          d[j]=b[i];
          break;
        }
      }
      count=j+1;
      if(count2<count){
        count2=count;
      }
    }
    System.out.println("Max Platforms required: "+ count2);
  }
}
