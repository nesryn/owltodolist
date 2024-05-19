/** @odoo-module */

import { registry } from "@web/core/registry";
const { Component,useState , onWillStart} = owl;
import { useService } from "@web/core/utils/hooks";

export class todoComponent extends Component {
    setup() {
    this.state = useState({
        task: {name:'',color:'',done:false},
        taskList:[],
        isEdit:false,
        activeId:false,
    });
    this.orm = useService("orm");
     onWillStart(async () => {
        await this.getAlltasks()
        })
}
    async getAlltasks(){
    this.state.taskList = await this.orm.searchRead( 'owl.todo.list', [],['name', 'color', 'done'], );
    }


    addTask(){
    this.state.task= {name:'',color:'',done:false}
        this.state.isEdit=false
//        this.state.activeId=false
    }
    editTask(task){
        console.log(task);
        console.log('this.state',this);
        console.log('this.state',this.state);
        this.state.isEdit = true
        this.state.task = task
//        this.state.task = {...task}
    }
    async saveTask(){
        console.log('saveTask',this.state.task)
        console.log('saveTask',this.state.isEdit)
    if (this.state.isEdit){
         await this.orm.write('owl.todo.list', [this.state.task.id],this.state.task ); // this.orm.write('model name', [id],{your data} );

    this.state.isEdit = false
    }
    else{
//    await this.orm.create('owl.todo.list', [{name: this.state.task.name ,color: this.state.task.color ,done:this.state.task.done}], );
     await this.orm.create('owl.todo.list', [this.state.task], ); // because this.state.task have the same field name
     await this.getAlltasks()
//       this.hide();
    }
    }

     async deleteTask(task){
     console.log('task',task)
     await this.orm.unlink("owl.todo.list", [task.id]);
     await this.getAlltasks()

//        this.state.activeId=false
    }

}

todoComponent.template = 'owl_todo_list.TodoListTemplate'
registry.category('actions').add('owl_todo_list.action_todo_list_js', todoComponent); //we will used in xml  model="ir.actions.client"