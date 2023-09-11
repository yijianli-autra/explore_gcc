#include "CCU6_Isr_Timer.h"


IFX_INTERRUPT(isrCCU6Timer, 0, ISR_PRIORITY_CCU6_INT1);
uint8 g_counter = 0;                                                        /* Variable to keep count of ISR calls  */

void isrCCU6Timer(void)
{
    switch(g_counter % 4)
    {
        case 1: /* Turn on LED1 only*/
            IfxPort_setPinState(LED1, IfxPort_State_low);
            IfxPort_setPinState(LED2, IfxPort_State_high);
            IfxPort_setPinState(LED3, IfxPort_State_high);
            IfxPort_setPinState(LED4, IfxPort_State_high);
            break;
        case 0: /* Turn on LED2 only */
            IfxPort_setPinState(LED1, IfxPort_State_high);
            IfxPort_setPinState(LED2, IfxPort_State_low);
            IfxPort_setPinState(LED3, IfxPort_State_high);
            IfxPort_setPinState(LED4, IfxPort_State_high);
            break;
        case 3: /* Turn on LED3 only */
            IfxPort_setPinState(LED1, IfxPort_State_high);
            IfxPort_setPinState(LED2, IfxPort_State_high);
            IfxPort_setPinState(LED3, IfxPort_State_low);
            IfxPort_setPinState(LED4, IfxPort_State_high);
            break;
        case 2: /* Turn on LED4 only */
            IfxPort_setPinState(LED1, IfxPort_State_high);
            IfxPort_setPinState(LED2, IfxPort_State_high);
            IfxPort_setPinState(LED3, IfxPort_State_high);
            IfxPort_setPinState(LED4, IfxPort_State_low);
            break;
        default: /* Turn off all LEDs */
            IfxPort_setPinState(LED1, IfxPort_State_high);
            IfxPort_setPinState(LED2, IfxPort_State_high);
            IfxPort_setPinState(LED3, IfxPort_State_high);
            IfxPort_setPinState(LED4, IfxPort_State_high);
            break;
    }
    g_counter++; /* Increase value of the counter each time the ISR is called */
}
