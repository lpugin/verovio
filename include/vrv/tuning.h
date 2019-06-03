/////////////////////////////////////////////////////////////////////////////
// Name:        tuning.h
// Author:      Laurent Pugin
// Created:     2019
// Copyright (c) Authors and others. All rights reserved.
/////////////////////////////////////////////////////////////////////////////

#ifndef __VRV_TUNING_H__
#define __VRV_TUNING_H__

#include "atts_frettab.h"
#include "object.h"

namespace vrv {

//----------------------------------------------------------------------------
// Tuning
//----------------------------------------------------------------------------

/**
 * This class models the MEI <tuning> element.
 */
class Tuning : public Object, public AttCourseLog {
public:
    /**
     * @name Constructors, destructors, and other standard methods
     * Reset method reset all attribute classes
     */
    ///@{
    Tuning();
    virtual ~Tuning();
    virtual Object *Clone() const { return new Tuning(*this); }
    virtual void Reset();
    virtual std::string GetClassName() const { return "Tuning"; };
    virtual ClassId GetClassId() const { return TUNING; };
    ///@}

    /**
     * Add an element to a element.
     */
    virtual void AddChild(Object *object);
    
    /**
     * Return the line for a the tuning and a given course.
     */
    int CalcPitchPos(int course);

protected:
    //
private:
    //
public:
    //
private:
    //
};

} // namespace vrv

#endif
