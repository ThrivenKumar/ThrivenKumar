import java.util.*;
class nim{
  int s1,s2,s3;
  nim(){
    s1=1;
    s2=4;
    s3=5;
  }
  int xorsum(int s1,int s2){
    int len,i;
    int flag=0,flag2=0;
    String stack1binaryrep=Integer.toBinaryString(s1);
    String stack2binaryrep=Integer.toBinaryString(s2);
    if((len=stack1binaryrep.length()-stack2binaryrep.length())>0)
      for(i=0;i<len;i++)
        stack2binaryrep="0"+stack2binaryrep;
    else if((len=stack1binaryrep.length()-stack2binaryrep.length())<0)
      for(i=0;i<-len;i++)
        stack1binaryrep="0"+stack1binaryrep;
    int xor=0;
    for(i=0;i<stack1binaryrep.length();i++){
      xor=xor+((int)stack1binaryrep.charAt(i)^(int)stack2binaryrep.charAt(i));
      xor=xor*10;
    }
    xor=xor/10;
    for(i=0;i<stack1binaryrep.length();i++){
      flag=xor%10;
      flag=flag*(int)Math.pow(2,i);
      flag2+=flag;
      xor=xor/10;
    }
    return flag2;
  }
  void computermove(){
    int count=0,count2;
    count=xorsum(s1,s2);
    if(count<s3&&count>=0){
      System.out.println("Computer picked "+ (s3-count) +" disks from pile 3");
      s3-=(s3-count);
      if(!Counter())
        System.out.println("!!!*** Computer Won ***!!!");
      return;
    }
    count=xorsum(s2,s3);
    if(count<s1&&count>=0){
      System.out.println("Computer picked "+ (s1-count) +" disks from pile 1");
      s1-=(s1-count);
      if(!Counter())
        System.out.println("!!!*** Computer Won ***!!!");
      return;
    }
    count=xorsum(s1,s3);
    if(count<s2&&count>=0){
      System.out.println("Computer picked "+ (s2-count) +" disks from pile 2");
      s2-=(s2-count);
      if(!Counter())
        System.out.println("!!!*** Computer Won ***!!!");
      return;
    }
    else{
      count=(int)Math.random()*(3-1)+1;
      if(count==1&&s1>0){
        count2=(int)Math.random()*(s1-1)+1;
        System.out.println("Computer picked "+ count2 +" disks from pile 2");
        s1-=count2;
      }
      else if(count==1&s2>0){
        count2=(int)Math.random()*(s2-1)+1;
        System.out.println("Computer picked "+ count2 +" disks from pile 2");
        s2-=count2;
      }
      else if(count==1&&s3>0){
        count2=(int)Math.random()*(s3-1)+1;
        System.out.println("Computer picked "+ count2 +" disks from pile 2");
        s3-=count2;
      }
      if(!Counter())
        System.out.println("!!!*** Computer Won ***!!!");
      return;
    }
  }
  boolean Counter(){
    if(s1>0||s2>0||s3>0)
      return true;
    else
      return false;
  }
  void Display(){
    System.out.println("--------------------------");
    System.out.println("   "+s1+" \t    "+s2+"  \t    "+s3);
    System.out.println(" Pile 1\t Pile 2\t Pile 3");
    System.out.println("--------------------------");
  }
  void playerMove(int n1,int n2){
    if(n1==1&&(s1-n2)>=0)
      s1-=n2;
    else if(n1==2&&(s2-n2)>=0)
      s2-=n2;
    else if(n1==3&&(s3-n2)>=0)
      s3-=n2;
    else{
      System.out.println("Can't remove disks from the pile!!!");
      System.out.println("Pick again");
      playerMove(new Scanner(System.in).nextInt(),new Scanner(System.in).nextInt());
    }
    if(!Counter())
      System.out.println("!!!*** Player Won ***!!!");
  }
  public static void main(String args[]){
    int move=2,input1,input2;
    nim n=new nim();
    Scanner s=new Scanner(System.in);
    while(n.Counter()){
      n.Display();
      System.out.println();
      if(move%2==0){
        System.out.println("Computer move ");
        n.computermove();
        System.out.println();
      }
      else{
        System.out.println("Your move  ");
        System.out.println("Pile No : ");
        input1=s.nextInt();
        System.out.println("Disk(s): ");
        input2=s.nextInt();
        n.playerMove(input1,input2);
        System.out.println();
      }
      move++;
    }
  }
}
