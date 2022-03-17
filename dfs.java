import java.util.*;

public class dfs{

    public static void addNumber(int a,ArrayList numbers){
        if (a==10){
            numbers.add(a);
            return ;
        }
            numbers.add(a);
            addNumber(++a, numbers);
    }
    public static void main(String args[]){
        int[][] n=new int[3][4];
        n[2][3]=4;
        int a=0;
        ArrayList<Integer> numbers= new ArrayList<Integer>();
        addNumber(a, numbers);
        System.out.println(numbers.size());
        // for (int i=0;i<NumberOfEdges;i++){
        //     System.out.println(a.get(i)[0]+ " " +a.get(i)[1]);
        // }
    }
}