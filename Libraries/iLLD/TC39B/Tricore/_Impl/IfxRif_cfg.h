/**
 * \file IfxRif_cfg.h
 * \brief RIF on-chip implementation data
 * \ingroup IfxLld_Rif
 *
 * \version iLLD_1_0_1_16_1
 * \copyright Copyright (c) 2018 Infineon Technologies AG. All rights reserved.
 *
 *
 *                                 IMPORTANT NOTICE
 *
 * Use of this file is subject to the terms of use agreed between (i) you or
 * the company in which ordinary course of business you are acting and (ii)
 * Infineon Technologies AG or its licensees. If and as long as no such terms
 * of use are agreed, use of this file is subject to following:
 *
 * Boost Software License - Version 1.0 - August 17th, 2003
 *
 * Permission is hereby granted, free of charge, to any person or organization
 * obtaining a copy of the software and accompanying documentation covered by
 * this license (the "Software") to use, reproduce, display, distribute,
 * execute, and transmit the Software, and to prepare derivative works of the
 * Software, and to permit third-parties to whom the Software is furnished to
 * do so, all subject to the following:
 *
 * The copyright notices in the Software and this entire statement, including
 * the above license grant, this restriction and the following disclaimer, must
 * be included in all copies of the Software, in whole or in part, and all
 * derivative works of the Software, unless such copies or derivative works are
 * solely in the form of machine-executable object code generated by a source
 * language processor.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
 * SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
 * FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
 * ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 *
 *
 *
 * \defgroup IfxLld_Rif RIF
 * \ingroup IfxLld
 * \defgroup IfxLld_Rif_Impl Implementation
 * \ingroup IfxLld_Rif
 * \defgroup IfxLld_Rif_Std Standard Driver
 * \ingroup IfxLld_Rif
 * \defgroup IfxLld_Rif_Impl_Enumerations Enumerations
 * \ingroup IfxLld_Rif_Impl
 * \defgroup IfxLld_Rif_Impl_Variables Global Variables
 * \ingroup IfxLld_Rif_Impl
 */

#ifndef IFXRIF_CFG_H
#define IFXRIF_CFG_H 1

/******************************************************************************/
/*----------------------------------Includes----------------------------------*/
/******************************************************************************/

#include "Cpu/Std/Ifx_Types.h"
#include "IfxRif_reg.h"

/******************************************************************************/
/*-----------------------------------Macros-----------------------------------*/
/******************************************************************************/

#define IFXRIF_NUM_MODULES (2)

/******************************************************************************/
/*--------------------------------Enumerations--------------------------------*/
/******************************************************************************/

/** \addtogroup IfxLld_Rif_Impl_Enumerations
 * \{ */
/** \brief List of the available RIF resources
 */
typedef enum
{
    IfxRif_Index_none = -1,  /**< \brief Not Selected */
    IfxRif_Index_0    = 0,   /**< \brief RIF index 0  */
    IfxRif_Index_1           /**< \brief RIF index 1  */
} IfxRif_Index;

/** \} */

/** \addtogroup IfxLld_Rif_Impl_Variables
 * \{ */

/******************************************************************************/
/*-------------------Global Exported Variables/Constants----------------------*/
/******************************************************************************/

IFX_EXTERN IfxModule_IndexMap IfxRif_cfg_indexMap[IFXRIF_NUM_MODULES];

/** \} */

#endif /* IFXRIF_CFG_H */
