
import java.util.Scanner;
public class  A4
{
    public static void main(String arga[])
    {
        Scanner s = new Scanner(System.in);
        int n=s.nextInt();
        if(n>2&&n%2==0)
        System.out.println("yes");
        else System.out.println("no");
        s.close();
    }
}