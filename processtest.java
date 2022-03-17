import java.io.*;
class processtest{
  public static void main(String args[]) throws Exception{
    System.out.println("Starting process");
    Process p1;
    p1=Runtime.getRuntime().exec("javac test.java");
    BufferedReader input= new BufferedReader(new InputStreamReader(System.in));
    String s;
    //while((s=output.readLine())!=null){
      s=input.readLine();
      if(s.contains("add")){
        
      }
      System.out.println(s);
    //}
  }
}
