/*
 * Curve_tracer_v2.cpp
 *
 * Created: 29-05-2021 21:57:28
 * Author : Vibhanshu Sharma
 */ 

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
int main(void)
{
	char c;
	int Vd=0;
	int Vr=0;
	int Vd_avg=0;
	int Vr_avg=0;
	UART_init(9600);
	ctc_init_pwm();
	adc_init();
	UART_SendString("\n\t Echo Test ");
	unsigned int z[256]={0, 4, 8,  12,  16,  20, 24, 28,  32, 36,  40, 44, 48, 52,  56,  60, 64,  68, 72, 76,  80,  84,  88,  92,  96,  100, 104,  108,  112,  116, 120,  124,128, 132, 136, 140,144,
	 148, 152,  156,  160,  164, 168,  172,  176, 180, 184, 188,  192,  196,  200,  204, 208,  212,  216,  220,  224,  228,  232,  236,  240,  244,  248, 252};
	c=UART_RxChar();
	if(c=='s')
	{
		_delay_ms(30);
		for(int i=0;i<64;i++)
		{	OCR0=z[i];
			_delay_ms(20);
			for (int p=0; p<8;p++)
				{	Vd=Vd+adc_read(1);
					Vr=Vr+adc_read(2);
						
				}
			//Vd=adc_read(1);
			//Vr=adc_read(2);
			//_delay_ms(50);
			Vd_avg=(Vd/8);
			Vr_avg=(Vr/8);
			usart_number(Vd_avg);
			UART_SendString(",");
			usart_number(Vr_avg);
			UART_SendString("\n");
			//_delay_ms(100);
		}
		UART_SendString("DONE");
		//usart_number(9999);
	}
}

