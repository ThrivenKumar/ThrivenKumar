import java.io.*;  
import java.security.*;  
import java.security.spec.AlgorithmParameterSpec;  
import javax.crypto.*; 
import javax.crypto.spec.IvParameterSpec; 
public class Des{
    private static Cipher encrypt;
    private static Cipher decrypt;
    private static final byte[] iv={11,22,33,44,55,66,77,99};
    public static void main(String args[]){
        String text="/Users/thrivenkumar/Desktop/plaintext.txt";
        String encryptedtext="/Users/thrivenkumar/Desktop/encryptedtext.txt";
        String decryptedtext="/Users/thrivenkumar/Desktop/decryptedtext.txt";
        try{
            SecretKey key=KeyGenerator.getInstance("DES").generateKey();
            AlgorithmParameterSpec asp=new IvParameterSpec(iv);
            encrypt=Cipher.getInstance("DES/CBC/PKCS5Padding");
            encrypt.init(Cipher.ENCRYPT_MODE,key,asp);
            decrypt=Cipher.getInstance("DES/CBC/PKCS5Padding");
            decrypt.init(Cipher.DECRYPT_MODE,key,asp);
            encryption(new FileInputStream(text),new FileOutputStream(encryptedtext));
            decryption(new FileInputStream(encryptedtext),new FileOutputStream(decryptedtext));
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
    public static void encryption(InputStream input,OutputStream output) throws IOException{
        output=new CipherOutputStream(output,encrypt);
        writeBytes(input, output);
    }
    public static void decryption(InputStream input,OutputStream output) throws IOException{
        input=new CipherInputStream(input, decrypt);
        writeBytes(input, output);
    }
    public static void writeBytes(InputStream input,OutputStream output) throws IOException{
        byte b[]=new byte[512];
        int readbytes=0;
        while((readbytes=input.read(b))>=0){
            output.write(b,0,readbytes);
        }
        output.close();
        input.close();
    }
}