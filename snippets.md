
```c
void removeLeadingZeros(char *str, char len){
    char *result;
    char i = 0;
    while (1){
        if (str[i] == 0x30){
            i++;
        }else {
            result = &str[i]; break;
            result = str + i; break;
        }
        if (i >+ len) break;
    }
    strcpy(str, result);
}
```