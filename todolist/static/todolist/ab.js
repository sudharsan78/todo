var TodoModel = Backbone.Model.extend({
  defaults: {
    task: null,
    completed: false
  }
});

var TodoCollection = Backbone.Collection.extend({
  model: TodoModel,
  urlRoot: 'http://localhost:8000/api/v1/todo',

});

var TodoListItemView = Backbone.View.extend({
  tagName: 'li',
  className: 'todotask',
  template: _.template($('#todotask-item-tmpl').html()),

  initialize: function() {
    this.listenTo(this.model, 'destroy', this.remove)
  },

  render: function() {
    var html = this.template(this.model.toJSON());
    this.$el.html(html);
    return this;
  },

  events: {
    'click .remove': 'onRemove'
  },

  onRemove: function() {
    this.model.destroy();
  }
});


var TodoListView = Backbone.View.extend({
  el: '#todo-app',

  initialize: function() {
    this.listenTo(this.collection, 'sync', this.render);
  },

  render: function() {
    var $list = this.$('ul.todo-list').empty();

    this.collection.each(function(model) {
      var item = new TodoListItemView({model: model});
      $list.append(item.render().$el);
    }, this);

    return this;
  },

  events: {
    'click .create': 'onCreate'
  },

  onCreate: function() {
    var $task = this.$('#todo-name');
    

    if ($newtask.val()) {
      this.collection.create({
        task: $newtask.val(),
        
      });

      $newtask.val('');
      
    }
  }
});
