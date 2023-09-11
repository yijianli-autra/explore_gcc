#ifndef CCU6_IR_CC_H
#define CCU6_IR_CC_H

#ifdef __cplusplus
  extern "C" {
#endif 

#include "IfxPort.h"
#include "IfxCcu6_Timer.h"
#include "CCU6_Isr_Timer.h"

extern void initPeripherals();
extern void startCCU6();

#ifdef __cplusplus
  }
#endif     

#endif
