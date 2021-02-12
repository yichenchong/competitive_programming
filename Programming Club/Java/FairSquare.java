
/**
 * Write a description of class FairSquare here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class FairSquare
{
    // instance variables - replace the example below with your own
    public static void main(String[] args)
    {
        // put your code here
        System.out.println(test(1,5));
    }
    public static int test(int num1,int num2) {
        int startInt=(int)Math.sqrt(num1);
        int endInt=(int)Math.sqrt(num2)+1;
        int count=0;
        for(int i=startInt;i<endInt;i++) {
            int square=(int)Math.pow(i,2);
            if(isFair(i)&&square>=num1&&square<=num2&&isFair(square)) {
                count++;
            }
        }
        return count;
    }
    public static boolean isFair(int num) {
        int orig=num;
        int reverse=num%10;
        num/=10;
        while(num>0) {
            reverse*=10;
            reverse+=num%10;
            num/=10;
        }
        return reverse==orig;
    }
}
