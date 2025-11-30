document.addEventListener('DOMContentLoaded', function(){
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click', function(e){
      e.preventDefault();
      const el = document.querySelector(this.getAttribute('href'));
      if (el) el.scrollIntoView({behavior:'smooth'});
    });
  });
});
