{% extends "./base.html" %}
{% block content %}
{% load static %}

<div class="main-div pt-0 header-bg-transparent header-logo-white">
  {% include './header.html' %}

  <!-- recipe -->
  <section id="recipe" class="pt-0"> 
    <div class="banner-cover">
      <img class="img-primary" src="{% static 'public/images/recipe-page/banner-cover/banner-top.jpg' %}">
      <div class="caption w-100 text-center">
        <div class="wrapper">
          <div class="row text-white">
            <div class="col-12" data-aos="fade-down" data-aos-duration="2000">
              <h3 class="font-lnterbold">RECIPE</h3>
              <h5 class="font-lnterbold">
                <a href="{%url 'web:common:home'%}">Home</a>
                <i class="fa fa-angle-right" aria-hidden="true"></i>
                <a>Recipe</a>
              </h5>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="wrapper pt-70">
      <div class="row justify-content-center text-center">
        <div class="col-lg-9">
          <div class="section-head" data-aos="fade-left" data-aos-duration="1000">
            <h1 class="text-blue font-lnterbold">RECIPES</h1>
            <h5 class="text-blue pt-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo, aliquid eaque. Commodi suscipit natus iste nesciunt, alias labore maxime perferendis quae excepturi accusamus animi soluta consectetur, tenetur ratione eos obcaecati.</h5>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          {%for i in recipe%}
          <div class="item bg-blue p-40 mt-25">
            <div class="row align-items-center">
              <div class="col-lg-7 col-md-6">
                <img class="img-fluid" src="{%if i.rec_image%}{{i.rec_image.first.image.url}}{%endif%}">
              </div>
              <div class="col-lg-4 offset-lg-1 col-md-6">
                <div class="title font-lnterbold">{{i.title}}</div>
                <div class="ingredients">Ingredients</div>
                <table>
                  <tbody>
                    {%for ing in i.rec_ind.all%}
                    <tr>
                      <td>{{ing.title}}</td>
                      <td>-</td>
                      <td>{{ing.amount}}</td>
                    </tr>
                    {%endfor%}
                  </tbody>
                </table>
                <button class="btn bg-white text-blue rounded-25 btn-icon btn-sm mt-25" type="button" data-bs-toggle="modal" data-bs-target="#recipe_modal{{forloop.counter}}">
                  <span>Read More</span>
                  <img src="{% static 'public/images/icons/right-arrow-blue.png' %}">
                </button>
              </div>
            </div>
          </div>



            <!-- recipe_modal -->
            <div class="modal fade recipe-modal" id="recipe_modal{{forloop.counter}}" tabindex="-1" aria-hidden="true">
              <div class="modal-dialog modal-xl">
                <div class="modal-content">
                  <div class="modal-header border-0 align-self-end">
                    <button type="button" class="btn text-blue btn-zoom-hover" data-bs-dismiss="modal" aria-label="Close">
                      <i class="fa fa-times-circle" aria-hidden="true"></i>
                    </button>
                  </div>
                  <div class="modal-body text-blue">
                    <div class="row">
                      <div class="col-lg-5">
                        {%for j in i.rec_image.all%}
                            <img class="img-fluid img-primary" src="{{j.image.url}}">
                        {%endfor%}
                      </div>
                      <div class="col-lg-7">
                        <h6>{{i.title}}</h6>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- /recipe_modal --> 

          {%endfor%}
        </div>
      </div>
    </div>

  </section>
  <!-- /recipe -->
  
  {% include './footer.html' %}
</div>
{% endblock %}