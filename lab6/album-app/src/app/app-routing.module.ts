import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AboutComponent } from './about/about.component';
import { AlbumDetailComponent } from './album-detail/album-detail.component';
import { AlbumPhotoComponent } from './album-photo/album-photo.component';
import { AlbumsComponent } from './albums/albums.component';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';

export const routes: Routes = [
{ path: '/home', component: HomeComponent },
{ path: '/about', component: AboutComponent },
{ path: '/albums', component: AlbumsComponent },
{ path: '/albums/:id', component: AlbumDetailComponent },
{ path: '/albums/:id/photos', component: AlbumPhotoComponent },
{ path: '', redirectTo: 'home', pathMatch: 'full'},
{ path: '**', component: NotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
