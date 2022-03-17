import java.io.*;
import java.util.*;
public class CCLab3
{
    public static void main(String[] args)throws IOException
    {
        String s;
        String s2[]=new String[20];
        char []op={'+','-','*','/','%','='};
        int i,j,flag=0,tmp=0;
        DataInputStream d=new DataInputStream(System.in);
        System.out.println("Enter Expression");
        s=d.readLine();
        char ch[]=s.toCharArray();
        for(i=0;i<s2.length;i++)
            s2[i]="";
        System.out.println("Tokens are");
        for(i=0;i<ch.length;i++)
        {
            flag=0;
            for(j=0;j<op.length;j++)
            {
                if(ch[i]==op[j])
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                System.out.print(ch[i]);
                s2[tmp]+=ch[i];
            }
            else if(flag==1)
            {
                tmp++;
                s2[tmp]+=op[j];
                System.out.print("\n"+op[j]+"\n");
                tmp++;
            }
        }
        System.out.println("\nElements in the stack are");
        Stack stk=new Stack();
        for(i=tmp;i>=0;i--)
        {
            stk.push(s2[i]);
        }
        for(i=tmp;i>=0;i--)
        {
            System.out.println(stk.pop());
        }
    }
}
