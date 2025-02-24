import java.util.Scanner;
public class A231 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n=s.nextInt();
        int flag=0,l=0;
        int [] a = new int [3];
        for(int j=0;j<n;j++)
        {
            flag=0;
        for (int i=0;i<3;i++)
        {
            a[i]=s.nextInt();
            if(a[i]==1)
            {
                flag++;
            }
        }
        if(flag>=2)
        {
            l++;
        }
    }
    System.out.println(l);

        s.close();
    }
    
}
