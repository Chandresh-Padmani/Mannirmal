(function ($) {
    'use strict';
    /*==================================================================
        [ Daterangepicker ]*/
    try {
        $('.js-datepicker').daterangepicker({
            "singleDatePicker": true,
            "showDropdowns": true,
            "autoUpdateInput": false,
            locale: {
                format: 'YYYY-MM-DD'
            },
        });
    
        var myCalendar = $('.js-datepicker');
        var isClick = 0;
    
        $(window).on('click',function(){
            isClick = 0;
        });
    
        $(myCalendar).on('apply.daterangepicker',function(ev, picker){
            isClick = 0;
            $(this).val(picker.startDate.format('YYYY-MM-DD'));
    
        });
    
        $('.js-btn-calendar').on('click',function(e){
            e.stopPropagation();
    
            if(isClick === 1) isClick = 0;
            else if(isClick === 0) isClick = 1;
    
            if (isClick === 1) {
                myCalendar.focus();
            }
        });
    
        $(myCalendar).on('click',function(e){
            e.stopPropagation();
            isClick = 1;
        });
    
        $('.daterangepicker').on('click',function(e){
            e.stopPropagation();
        });
    
    
    } catch(er) {console.log(er);}
    /*[ Select 2 Config ]
        ===========================================================*/
    
    try {
        var selectSimple = $('.js-select-simple');
    
        selectSimple.each(function () {
            var that = $(this);
            var selectBox = that.find('select');
            var selectDropdown = that.find('.select-dropdown');
            selectBox.select2({
                dropdownParent: selectDropdown
            });
        });
    
    } catch (err) {
        console.log(err);
    }
    

})(jQuery);


const registration = document.getElementById('registration');


// add event
// registration.addEventListener('submit', (event) => {
//     event.preventDefault();
//     validate();
// });

function validateReg() {

        const firstname = document.getElementById('firstname');
        const lastname = document.getElementById('lastname');
        const email = document.getElementById('email');
        const address = document.getElementById('address');
        const country_code = document.getElementById('country_code');
        const number = document.getElementById('number');
        const city = document.getElementById('city');
        const country = document.getElementById('country');
        const postal = document.getElementById('postal');
        const description = document.getElementById('description');

        const firstnameValue = firstname.value.trim();

        var validation_status = true;

        if(firstnameValue === '') {
            setErrormsg(firstname, '* Firstname cannot be blank');
            validation_status = false;
        } else if(!isName(firstnameValue)) {
            setErrormsg(firstname, '* Names may only contain alphabets, with length 3 to 30');
            validation_status = false;
        } else {
            setSuccessMsg(firstname);
        }

    
        const lastnameValue = lastname.value.trim();
    
        if(lastnameValue === '') {
            setErrormsg(lastname, '* Lastname cannot be blank');
            validation_status = false;
        } else if(!isName(lastnameValue)) {
            setErrormsg(lastname, '* Names may only contain alphabets, with length 3 to 30');
            validation_status = false;
        } else {
            setSuccessMsg(lastname);
        }


        const emailValue = email.value.trim();

        if(emailValue === '') {
            setErrormsg(email, '* Email cannot be blank');
            validation_status = false;
        } else if(!isEmail(emailValue)) {
            setErrormsg(email, '* Not a valid Email');
            validation_status = false;
        } else {
            setSuccessMsg(email);
        }

        const addressValue = address.value.trim();
    
        if(addressValue === '') {
            setErrormsg(address, '* Address cannot be blank');
            validation_status = false;
        } else if(addressValue.length < 3) {
            setErrormsg(address, '* Address must be atleast 25 characters');
            validation_status = false;
        } else if(addressValue.length > 100) {
            setErrormsg(address, '* Too long address');
            validation_status = false;
        }else {
            setSuccessMsg(address);
        }

        const numberValue = number.value.trim();

        if(numberValue === '') {
            setErrormsg(number, '* Number cannot be blank');
            validation_status = false;
        } else if(!isNumber(numberValue)) {
            setErrormsg(number, '* Not a valid contact number');
            validation_status = false;
        } else {
            setSuccessMsg(number);
        }

        const cityValue = city.value.trim();
        
        if(cityValue === '') {
            setErrormsg(city, '* City cannot be blank');
            validation_status = false;
        } else if(!isName(cityValue)) {
            setErrormsg(city, '* City must be atleast 3 and atmost 30 characters');
            validation_status = false;
        } else {
            setSuccessMsg(city);
        }

        const countryValue = country.value.trim();
        
        if(countryValue === '') {
            setErrormsg(country, '* Country cannot be blank');
            validation_status = false;
        } else if(!isName(countryValue)) {
            setErrormsg(country, '* Country must be atleast 3 and atmost 30 characters');
            validation_status = false;
        } else {
            setSuccessMsg(country);
        }

        const postalValue = postal.value.trim();
        
        if(postalValue === '') {
            setErrormsg(postal, '* Postal code cannot be blank');
            validation_status = false;
        } else if(!isPostal(postalValue)) {
            setErrormsg(postal, '* Not a valid postal code');
            validation_status = false;
        } else {
            setSuccessMsg(postal);
        }

        const desValue = description.value.trim();
        
        if(desValue.length > 300) {
            setErrormsg(description, '* Too long description');
            validation_status = false;
        } else {
            setSuccessMsg(description);
        }
    
        return validation_status;

}

function validateIdeas() {

        const firstname = document.getElementById('idea-firstname');
        const lastname = document.getElementById('idea-lastname');
        const email = document.getElementById('idea-email');        
        const country_code = document.getElementById('country_code');
        const number = document.getElementById('idea-number');
        const feedback = document.getElementById('idea-feedback');
        const thoughts = document.getElementById('idea-thoughts');


    const firstnameValue = firstname.value.trim();

    if(firstnameValue === '') {
        setErrormsg(firstname, '* Firstname cannot be blank');
        return false;
    } else if(!isName(firstnameValue)) {
        setErrormsg(firstname, '* Names may only contain alphabets, with length 3 to 30');
        return false;
    } else {
        setSuccessMsg(firstname);
    }


    const lastnameValue = lastname.value.trim();

    if(lastnameValue === '') {
        setErrormsg(lastname, '* Lastname cannot be blank');
        return false;
    } else if(!isName(lastnameValue)) {
        setErrormsg(lastname, '* Names may only contain alphabets, with length 3 to 30');
        return false;
    } else {
        setSuccessMsg(lastname);
    }


    const emailValue = email.value.trim();

    if(emailValue === '') {
        setErrormsg(email, '* Email cannot be blank');
        return false;
    } else if(!isEmail(emailValue)) {
        setErrormsg(email, '* Not a valid Email');
        return false;
    } else {
        setSuccessMsg(email);
    }

    
    const numberValue = number.value.trim();

    if(numberValue === '') {
        setErrormsg(number, '* Number cannot be blank');
        return false;
    } else if(!isNumber(numberValue)) {
        setErrormsg(number, '* Not a valid contact number');
        return false;
    } else {
        setSuccessMsg(number);
    }

    
    const feedbackValue = feedback.value.trim();
    
    if(feedbackValue.length > 300) {
        setErrormsg(feedback, '* Too long feedback');
        return false;
    } else {
        setSuccessMsg(feedback);
    }


    const thoughtsValue = thoughts.value.trim();
    
    if(thoughtsValue === '') {
        setErrormsg(thoughts, '* Thoughts cannot be blank');
        return false;
    } else if(thoughtsValue.length < 30) {
        setErrormsg(thoughts, '* Thoughts must be atleast 30 characters');
        return false;
    } else if(thoughtsValue.length > 300) {
        setErrormsg(thoughts, '* Too long thoughts');
        return false;
    } else {
        setSuccessMsg(thoughts);
    }


}

function setErrormsg(input, errormsg) {
    const formField = input.parentElement;
    const small = formField.querySelector('small');
    formField.className = 'form-group form-field status-group-icon error';
    small.innerText = errormsg;
}

function setSuccessMsg(input) {
	const formField = input.parentElement;
	formField.className = 'form-group form-field status-group-icon success';
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

function isName(name) {
    return /^[a-zA-Z ]{3,31}$/.test(name);
}

function isNumber(number) {
    return /^([0-9]{8,15})$/.test(number);
}

function isPostal(postal) {
    return /^[0-9]{0,6}$/.test(postal);
}

function isDetail(detail) {
    return /^([a-z A-Z0-9\'":()&$%-_@+#*=.;,?!\s]*){3,300}$/.test(detail);
}