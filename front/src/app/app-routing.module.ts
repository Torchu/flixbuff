import { RouterModule, Routes } from '@angular/router';
import { BaseComponent } from './base/base.component';
import { NgModule } from '@angular/core';
import { ShowDetailsComponent } from './show/show-details/show-details.component';
import { ShowListComponent } from './show/show-list/show-list.component';
import { UserDetailsComponent } from './user/user-details/user-details.component';
import { UserListComponent } from './user/user-list/user-list.component';

const routes: Routes = [
  {
    path: '',
    component: BaseComponent,
    children: [
      {
        path: '',
        component: ShowListComponent
      },
      {
        path: 'shows/:id',
        component: ShowDetailsComponent
      },
      {
        path: 'users',
        component: UserListComponent
      },
      {
        path: 'users/:id',
        component: UserDetailsComponent
      },
      {
        path: '**',
        redirectTo: ''
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
