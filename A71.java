
import java.util.*;
public class A71 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t=s.nextInt();
        while(t-->0)
        {
            String st = s.next();
            if(st.length()<=10)
            {
                System.out.println(st);
            }
            else
            {
                char[] a = st.toCharArray();
                int l = a.length-2;
                System.out.println(a[0]+""+l+""+a[a.length-1]);
            }
        }
       
        s.close();
    }
}
