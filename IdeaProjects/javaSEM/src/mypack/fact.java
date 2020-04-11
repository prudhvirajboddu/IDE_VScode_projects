package mypack;

public class fact {
    public long factorial(int num){
        int fact=1;
        for (int i=num;i>1;i--){
            fact=fact*i;
        }
     return fact;
    }
}
