
(function() {
    "use strict";
  
/**
 * Easy selector helper function
 */
const select = (el, all = false) => {
    el = el.trim()
    if (all) {
    return [...document.querySelectorAll(el)]
    } else {
    return document.querySelector(el)
    }
}
/**
   * Menu isotope and filter
   */
window.addEventListener('load', () => {
    let menuContainer = select('.menu-container');
    if (menuContainer) {
      let menuIsotope = new Isotope(menuContainer, {
        itemSelector: '.menu-item',
        layoutMode: 'fitRows'
      });

      let menuFilters = select('#menu-flters li', true);

      on('click', '#menu-flters li', function(e) {
        e.preventDefault();
        menuFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');
        
        menuIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });

      }, true);
    }

  });
})()



const countDownDate = new Date("Nov 31,2022 00:00:00").getTime();  


var countDownFunction =setInterval(function() {
    var now = new Date().getTime();

    var distance = countDownDate-now;

    var days = Math.floor(distance /(1000*60*60*24));

    var hours = Math.floor((distance % (1000*60*60*24))/(1000*60*60));

    var minutes = Math.floor((distance % (1000*60*60))/(1000*60));

    var seconds = Math.floor((distance % (1000*60))/1000);

    document.getElementById("timer").innerHTML = 
    days+"D "+hours+"H "+minutes+"M "+seconds+"S ";


    if (distance <= 0){
        clearInterval(countDownFunction);
        document.getElementById("timer").innerHTML = "Sales end"
    }
},1000)


