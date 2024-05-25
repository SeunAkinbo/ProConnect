$(document).ready(function() {
    // Smooth scroll for internal links
    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if(target.length) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top
            }, 1000);
        }
    });

    // Tab functionality
    $('.tab-link').on('click', function(event) {
        event.preventDefault();
        var tabId = $(this).data('tab');
        $('.tab-content').hide();
        $('#' + tabId).show();
    });

    // Skill Search button click event
    $('#search-btn').on('click', function() {
        var selectedSkill = $('#skills-dropdown').val();
        getProfiles(selectedSkill);
    });

    // Update Profile form submission
    $('#update-form').on('submit', function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '/update',
            data: formData,
            success: function() {
                alert('Profile updated successfully!');
                location.reload(); // Reload the page to reflect the changes
            },
            error: function() {
                alert('There was an error updating the profile.');
            }
        });
    });

    // Add Skill button click event
    $('#add-skill').on('click', function() {
        $('#skills-container').append(`
            <div class="skill-entry">
                <input type="text" name="skills[]" placeholder="Skill" required>
                <input type="text" name="duration[]" placeholder="Duration (e.g., 5 years)" required>
                <button type="button" class="remove-skill">Remove</button>
            </div>
        `);
    });

    // Remove Skill button click event
    $('#skills-container').on('click', '.remove-skill', function() {
        $(this).closest('.skill-entry').remove();
    });

    // Function to get profiles based on selected skill
    function getProfiles(skill) {
        $.ajax({
            type: 'GET',
            url: '/profiles',
            data: { skill: skill },
            success: function(profiles) {
                displayProfiles(profiles);
            },
            error: function() {
                alert('There was an error retrieving the profiles.');
            }
        });
    }

    // Function to display profiles in the container
    function displayProfiles(profiles) {
        var container = $('#profiles-container');
        container.empty();
        profiles.forEach(function(profile) {
            var profileHtml = `
                <div class="profile" data-profile='${JSON.stringify(profile)}'>
                    <img src="${profile.avatar}" alt="${profile.name}">
                    <div class="profile-info">
                        <h3>${profile.name}</h3>
                        <p>${profile.description}</p>
                    </div>
                </div>
            `;
            container.append(profileHtml);
        });

        // Add click event to each profile to show modal
        $('.profile').on('click', function() {
            var profileData = $(this).data('profile');
            showModal(profileData);
        });
    }

    // Function to show modal with profile details
    function showModal(profile) {
        var modal = $('#profile-modal');
        var modalProfile = modal.find('.modal-profile');

        var skillsList = profile.skills.map(skill => `<li>${skill}</li>`).join('');

        var profileDetails = `
            <img src="${profile.avatar}" alt="${profile.name}">
            <h3>${profile.name}</h3>
            <p>${profile.description}</p>
            <p>Address: ${profile.address}</p>
            <p>Payment: ${profile.payment}</p>
            <p>Availability: ${profile.availability}</p>
            <div class="skills">
                <h4>Skills:</h4>
                <ul>${skillsList}</ul>
            </div>
            <p>Reviews: ${profile.reviews}</p>
            <button id="connect-btn" class="connect-btn">Connect</button>
            <div id="contact-info" style="display:none;">
                <p>Email: <a href="mailto:${profile.email}">${profile.email}</a></p>
                <p>LinkedIn: <a href="${profile.linkedin}" target="_blank">${profile.linkedin}</a></p>
                <p>GitHub: <a href="${profile.github}" target="_blank">${profile.github}</a></p>
            </div>
            <button id="collaborate-btn" class="collaborate-btn">Collaborate</button>
        `;

        modalProfile.html(profileDetails);
        modal.show();

        // Connect button click event
        $('#connect-btn').on('click', function() {
            $('#contact-info').toggle();
        });

        // Add click event for "Collaborate" button
        $('#collaborate-btn').on('click', function() {
            addToTeamView(profile);
            alert('Profile added to your team!');
        });
    }

    // Function to add profile to team view
    function addToTeamView(profile) {
        var teamContainer = $('#team-container');
        var teamHtml = `
            <div class="team-member">
                <img src="${profile.avatar}" alt="${profile.name}">
                <div class="team-info">
                    <h3>${profile.name}</h3>
                    <p>${profile.description}</p>
                </div>
            </div>
        `;
        teamContainer.append(teamHtml);
    }

    // Close modal on click of the close button
    $('.modal .close').on('click', function() {
        $('#profile-modal').hide();
    });

    // Close modal on click outside of the modal content
    $(window).on('click', function(event) {
        if ($(event.target).is('#profile-modal')) {
            $('#profile-modal').hide();
        }
    });

    // Handle tab switching
    $('.tab-link').click(function(event) {
        event.preventDefault();
        var tabID = $(this).attr('data-tab');
        
        $('.tab-content').hide();
        $('#' + tabID).show();
        
        $('.tab-link').removeClass('active');
        $(this).addClass('active');
    });

    // Show the first tab by default
    $('.tab-link').first().click();

    // Handle modal close
    $('.close').click(function() {
        $('.modal').hide();
    });

    // Add click event for "Collaborate" button
    $('#team-view').on('click', function() {
        alert('Search skills and click collaborate to add members to your team!');
    });

    //Handling Tabs and Form Submissions
    $('.tab-link').click(function() {
        var tab_id = $(this).attr('data-tab');
        $('.tab-content').hide();
        $('#' + tab_id).show();
    });
});
