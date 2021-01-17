#define F_CPU 16000000UL /* Define frequency here its 8MHz */
#include <avr/io.h>
#include <util/delay.h>
#include <stdlib.h>
#include <stdio.h>
//#define USART_BAUDRATE 9600
#define BAUD_PRESCALE (((F_CPU / (USART_BAUDRATE * 16UL))) - 1)
void UART_init(long USART_BAUDRATE)
{
UCSRB |= (1 << RXEN) | (1 << TXEN);/* Turn on transmission and reception */
UCSRC |= (1 << URSEL) | (1 << UCSZ0) | (1 << UCSZ1);/* Use 8-bit character sizes */
UBRRL = BAUD_PRESCALE; /* Load lower 8-bits of the baud rate value */
UBRRH = (BAUD_PRESCALE >> 8); /* Load upper 8-bits*/
}
unsigned char UART_RxChar()
{
while ((UCSRA & (1 << RXC)) == 0);/* Wait till data is received */
return(UDR); /* Return the byte*/
}
void UART_TxChar(char ch)
{
while (! (UCSRA & (1<<UDRE))); /* Wait for empty transmit buffer*/
UDR = ch ;
}
void UART_SendString(char *str)
{
unsigned char j=0;
while (str[j]!=0) /* Send string till null */
{
UART_TxChar(str[j]);
j++;
}
}
void usart_number(unsigned int value) //USART Function to transmit integer data over USART Protocol
{
int d=0;
unsigned char ch[4]={0};
for(int i=0;i<4;i++)
{
d=value%10;
ch[i]=d+48;
value=value/10;
}
UART_TxChar(ch[3]);
UART_TxChar(ch[2]);
UART_TxChar(ch[1]);
UART_TxChar(ch[0]);
}
void ctc_init_pwm()
{
TCCR0 =0x69;
DDRB=0b00001000;
}
void adc_init()
{
ADMUX=(1<<REFS0); /*voltage is choose as vcc*/
ADCSRA=(1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}
unsigned int adc_read(unsigned char channel)
{
ADMUX=0X40|channel;
ADCSRA|=(1<<ADSC);
while(!(ADCSRA&(1<<ADIF)));
ADCSRA|=(1<<ADIF);
return ADC;
}
int main()
{
char c;
int Vd=0;
int Vr=0;
UART_init(9600);
ctc_init_pwm();
adc_init();
UART_SendString("\n\t Echo Test ");
unsigned int z[256]={0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
145, 146, 147, 148,149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255};
c=UART_RxChar();
if(c=='s')
{
_delay_ms(50);
for(int i=0;i<256;i++)
{OCR0=z[i];
_delay_ms(10);
Vd=adc_read(1);
Vr=adc_read(2);
//_delay_ms(50);
usart_number(Vd);
UART_SendString(",");
usart_number(Vr);
UART_SendString("\n");
//_delay_ms(100);
}
UART_SendString("DONE");
//usart_number(9999);
}
}
