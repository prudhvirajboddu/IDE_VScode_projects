class ExceptionsA{
    static void genException(){
        int num[]= {4,8,16,32,64,128,256};
        int div[]= {2,0,4,4,0,8};

        for(int i=0; i<num.length; i++){
            System.out.println(num[i] + "/" +
                    div[i] + "is" +
                    num[i]/div[i]);
        }
    }
}
class ExceptionsB extends ExceptionsA{
    ExceptionsB(){
        String zero;
        zero = "Division by zero not allowed";
    }
}
class ExceptionsC extends ExceptionsB{
    ExceptionsC(){
        String array;
        array = "Divisor element not found";
    }
}
public class ExceptionTest {
    public static void main(String[] args){
        try {
            ExceptionsA.genException();
        }
        catch (ArithmeticException zero){
            System.out.printf("%s",zero);
        }
        catch (ArrayIndexOutOfBoundsException array){
            System.out.printf("%s",array);
        }//end catch
    }//end class
}//end method

