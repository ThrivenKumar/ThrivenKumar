interface bird{
     int flyspeed();
}

class bird2{
    boolean canThisFly(){
        return true;
    }
}
public class eagle extends bird2 implements bird  {
    @Override
    boolean canThisFly(){
        return false;
    }
    public int flyspeed(){
        return 1;
    }
    public static void main(String args[]){
        System.out.println("Hello this is a eagle");
    }

}