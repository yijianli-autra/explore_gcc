#include "IfxPort.h"
#include "IfxCcu6_Timer.h"

#define ISR_PRIORITY_CCU6_INT1  40                                          /* Priority for interrupt ISR           */

/* LEDs */
#define LED1                    &MODULE_P13,0                               /* LED D107                             */
#define LED2                    &MODULE_P13,1                               /* LED D108                             */
#define LED3                    &MODULE_P13,2                               /* LED D109                             */
#define LED4                    &MODULE_P13,3                               /* LED D110                             */
